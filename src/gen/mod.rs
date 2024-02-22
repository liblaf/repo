use std::path::Path;

use crate::schema::Update;

mod cargo;
mod github_actions;

pub use cargo::Cargo;
pub use github_actions::GitHubActions;

pub trait Generator {
    fn gen(&self, path: &Path) -> anyhow::Result<Vec<Update>>;
}
