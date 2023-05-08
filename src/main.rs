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

fn main() {
    const STAR_CATALOG_PATH: &str = "catalog/hygdata_v3.csv";

    println!("Loading Star catalog from '{}'...", STAR_CATALOG_PATH);
    let catalog = StarCatalog::new(STAR_CATALOG_PATH);
    println!("Done. Number of catalog items: {}", catalog.stars.len());

    const WIDTH: usize = 500;
    const HEIGHT: usize = 500;
    let canvas = DMatrix::repeat(HEIGHT, WIDTH, 1000);

    let mut window = Window::new("Simulator", WIDTH, HEIGHT, WindowOptions::default())
        .unwrap_or_else(|e| {
            panic!("{}", e);
        });

    // Limit to max ~60 fps update rate
    window.limit_update_rate(Some(Duration::from_micros(16600)));

    while window.is_open() && !window.is_key_down(Key::Escape) {
        window
            .update_with_buffer(canvas.as_slice(), WIDTH, HEIGHT)
            .unwrap();
    }
}
