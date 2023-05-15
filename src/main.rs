use std::{collections::HashMap, time::Duration};

use minifb::{Key, Window, WindowOptions};
use nalgebra::{DMatrix, Vector3};

#[derive(Debug)]
struct Star {
    orientation: (f64, f64),
    absmag: f64,
}

struct StarCatalog {
    stars: Vec<Star>,
}

impl StarCatalog {
    fn new(filepath: &'static str) -> Self {
        Self {
            stars: csv::Reader::from_path(filepath)
                .unwrap()
                .deserialize()
                .map(|item| {
                    let fields: HashMap<String, String> = item.unwrap();

                    Star {
                        orientation: (
                            fields["rarad"].parse().unwrap(),
                            fields["decrad"].parse().unwrap(),
                        ),
                        absmag: fields["absmag"].parse().unwrap(),
                    }
                })
                .collect(),
        }
    }
}

struct ImageSensor {
    /// sensor size in Width x Height pixels
    size: (usize, usize),
    /// captured image arranged in column-by-columns 10 bit values
    image: DMatrix<u32>,
}

impl ImageSensor {
    fn new(size: (usize, usize)) -> Self {
        Self {
            size,
            image: DMatrix::zeros(size.0, size.1),
        }
    }

    fn project(&self, fov: &(f64, f64), star: &Star) -> (i32, i32) {
        (0, 0)
    }

    fn capture(&mut self, fov: &(f64, f64), orientation: &(f64, f64), stars: &Vec<Star>) {
        let (width, height) = self.size;

        for s in stars {
            if s.absmag > 5.0 {
                let (u, v) = self.project(fov, s);
                if u >= 0 && v >= 0 && u < width as i32 && v < height as i32 {
                    self.image[(u as usize, v as usize)] = 10000;
                }
            }
        }
    }
}

struct StarTracker {
    /// rectangular FOV (in radians)
    fov: (f64, f64),
    /// orientation in ECI coordinate frame
    orientation: (f64, f64),
    /// star catalog
    catalog: StarCatalog,
    /// image sensor
    image_sensor: ImageSensor,
}

impl StarTracker {
    fn new(catalog: StarCatalog) -> Self {
        const FOV_DEG: (f64, f64) = (15.0, 15.0);
        const INITIAL_ORIENTATION: (f64, f64) = (0.0, 0.0);
        const IMAGE_SENSOR_SIZE: (usize, usize) = (640, 480);

        Self {
            fov: (FOV_DEG.0.to_radians(), FOV_DEG.1.to_radians()),
            orientation: INITIAL_ORIENTATION,
            catalog,
            image_sensor: ImageSensor::new(IMAGE_SENSOR_SIZE),
        }
    }

    fn update(&mut self) {
        self.image_sensor
            .capture(&self.fov, &self.orientation, &self.catalog.stars);
    }

    fn update_orientation_by(&mut self, increment: &(f64, f64)) {
        self.orientation.0 += increment.0;
        self.orientation.1 += increment.1;
        println!("{:?}", self.orientation);
    }
}

fn main() {
    const STAR_CATALOG_PATH: &str = "catalog/hygdata_v3.csv";

    println!("Loading Star catalog from '{}'...", STAR_CATALOG_PATH);
    let catalog = StarCatalog::new(STAR_CATALOG_PATH);
    println!("Done. Number of catalog items: {}", catalog.stars.len());

    let mut tracker = StarTracker::new(catalog);

    let (width, height) = tracker.image_sensor.size;
    let mut window = Window::new("Simulator", width, height, WindowOptions::default())
        .unwrap_or_else(|e| {
            panic!("{}", e);
        });

    // limit to max ~60 fps update rate
    window.limit_update_rate(Some(Duration::from_micros(16600)));

    while window.is_open() && !window.is_key_down(Key::Escape) {
        window.get_keys().iter().for_each(|key| match key {
            Key::Up => tracker.update_orientation_by(&(1.0, 0.0)),
            Key::Right => tracker.update_orientation_by(&(0.0, 1.0)),
            Key::Down => tracker.update_orientation_by(&(-1.0, 0.0)),
            Key::Left => tracker.update_orientation_by(&(0.0, -1.0)),
            _ => (),
        });

        tracker.update();

        window
            .update_with_buffer(tracker.image_sensor.image.as_slice(), width, height)
            .unwrap();
    }
}
