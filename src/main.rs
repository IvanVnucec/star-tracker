use std::{collections::HashMap, time::Duration};

use minifb::{Key, Window, WindowOptions};
use nalgebra::DMatrix;

const WIDTH: usize = 500;
const HEIGHT: usize = 500;
const STARS_CATALOG_PATH: &str = "catalog/hygdata_v3.csv";

struct Star {
    ra: f64,
    dec: f64,
    absmag: f64,
}

fn load_stars_from_catalog(catalog_path: &str) -> Result<Vec<Star>, csv::Error> {
    let stars = csv::Reader::from_path(catalog_path)?
        .deserialize()
        .filter_map(|s| {
            let vals: HashMap<String, String> = s.unwrap();

            let ra = vals["ra"].parse().ok()?;
            let dec = vals["dec"].parse().ok()?;
            let absmag = vals["absmag"].parse().ok()?;

            Some(Star { ra, dec, absmag })
        })
        .collect();

    Ok(stars)
}

fn main() {
    println!("Loading the Star catalog...");
    let stars = load_stars_from_catalog(STARS_CATALOG_PATH).unwrap();
    println!("Done. Number of catalog items: {}", stars.len());

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
