use std::{collections::HashMap, path::Path};

use crate::schema::{CommitMessage, Group, Update};

use super::Generator;

pub struct Cargo;

impl Generator for Cargo {
    fn gen(&self, path: &Path) -> anyhow::Result<Vec<Update>> {
        if path.join("Cargo.toml").exists() {
            Ok(vec![Update {
                package_ecosystem: "cargo".to_string(),
                directory: "/".to_string(),
                schedule: Default::default(),
                commit_message: Some(CommitMessage::new("cargo")),
                groups: HashMap::from([("cargo".to_string(), Group::default())]),
            }])
        } else {
            Ok(vec![])
        }
    }
}
