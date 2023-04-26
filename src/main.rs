use minifb::{Key, Window, WindowOptions};
use nalgebra::DMatrix;

const WIDTH: usize = 500;
const HEIGHT: usize = 500;

fn main() {
    let canvas = DMatrix::repeat(HEIGHT, WIDTH, 1000);

    let mut window = Window::new("Simulator", WIDTH, HEIGHT, WindowOptions::default())
        .unwrap_or_else(|e| {
            panic!("{}", e);
        });

    // Limit to max ~60 fps update rate
    window.limit_update_rate(Some(std::time::Duration::from_micros(16600)));

    while window.is_open() && !window.is_key_down(Key::Escape) {
        window
            .update_with_buffer(canvas.as_slice(), WIDTH, HEIGHT)
            .unwrap();
    }
}
