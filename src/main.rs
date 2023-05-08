use std::{collections::HashMap, time::Duration};

use minifb::{Key, Window, WindowOptions};
use nalgebra::{DMatrix, Vector3};

#[derive(Debug)]
struct Star {
    ra: f64,
    dec: f64,
    absmag: f64,
}

impl Star {
    /// Returns the Star unit vector defined in the Earth-centered inertial
    /// (ECI) coordinate frame.
    fn xyz(&self) -> Vector3<f64> {
        Vector3::new(
            self.ra.cos() * self.dec.cos(),
            self.ra.sin() * self.dec.cos(),
            self.dec.sin(),
        )
    }
}

struct StarCatalog {
    stars: Vec<Star>,
}

impl StarCatalog {
    fn new(filepath: &'static str) -> StarCatalog {
        StarCatalog {
            stars: csv::Reader::from_path(filepath)
                .unwrap()
                .deserialize()
                .map(|item| {
                    let fields: HashMap<String, String> = item.unwrap();

                    Star {
                        ra: fields["rarad"].parse().unwrap(),
                        dec: fields["decrad"].parse().unwrap(),
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
    fn new(size: (usize, usize)) -> ImageSensor {
        ImageSensor {
            size,
            image: DMatrix::zeros(size.0, size.1),
        }
    }

    fn capture(&self, orientation: Vector3<f64>, stars: Vec<Star>) {
        todo!("implement camera transformations")
    }
}

struct StarTracker {
    /// rectangular FOV (in radians)
    fov: (f64, f64),
    /// orientation unit vector in ECI coordinate frame
    orientation: Vector3<f64>,
    /// star catalog
    catalog: StarCatalog,
    /// image sensor
    image_sensor: ImageSensor,
}

impl StarTracker {
    fn new(catalog: StarCatalog) -> StarTracker {
        const FOV_DEG: (f64, f64) = (15.0, 15.0);
        const INITIAL_ORIENTATION: Vector3<f64> = Vector3::new(1.0, 0.0, 0.0);
        const IMAGE_SENSOR_SIZE: (usize, usize) = (640, 480);

        StarTracker {
            fov: (FOV_DEG.0.to_radians(), FOV_DEG.1.to_radians()),
            orientation: INITIAL_ORIENTATION,
            catalog,
            image_sensor: ImageSensor::new(IMAGE_SENSOR_SIZE),
        }
    }
}

fn main() {
    const STAR_CATALOG_PATH: &str = "catalog/hygdata_v3.csv";

    println!("Loading Star catalog from '{}'...", STAR_CATALOG_PATH);
    let catalog = StarCatalog::new(STAR_CATALOG_PATH);
    println!("Done. Number of catalog items: {}", catalog.stars.len());

    let tracker = StarTracker::new(catalog);

    let (width, height) = tracker.image_sensor.size;
    let mut window = Window::new("Simulator", width, height, WindowOptions::default())
        .unwrap_or_else(|e| {
            panic!("{}", e);
        });

    // limit to max ~60 fps update rate
    window.limit_update_rate(Some(Duration::from_micros(16600)));

    while window.is_open() && !window.is_key_down(Key::Escape) {
        window
            .update_with_buffer(tracker.image_sensor.image.as_slice(), width, height)
            .unwrap();
    }
}
