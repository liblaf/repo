use std::path::Path;

pub fn exists(dir: &Path, pattern: &str) -> bool {
    glob::glob(dir.join(pattern).to_str().unwrap())
        .unwrap()
        .count()
        > 0
}
