use std::{collections::HashMap, path::Path};

use crate::schema::{CommitMessage, Update};

use super::Generator;

pub struct GitHubActions;

impl Generator for GitHubActions {
    fn gen(&self, path: &Path) -> anyhow::Result<Vec<Update>> {
        let mut updates = vec![];
        let path = path.canonicalize()?;
        if crate::utils::exists(path.as_path(), ".github/workflows/*.yaml")
            || crate::utils::exists(path.as_path(), "action.yaml")
        {
            updates.push(Update {
                package_ecosystem: "github-actions".to_string(),
                directory: "/".to_string(),
                schedule: Default::default(),
                commit_message: Some(CommitMessage::new("github-actions")),
                groups: HashMap::from([("github-actions".to_string(), Default::default())]),
            });
        }
        for file in
            glob::glob(path.join(".github/actions/*/action.yaml").to_str().unwrap()).unwrap()
        {
            let file = file?;
            let dir = file.parent().unwrap();
            updates.push(Update {
                package_ecosystem: "github-actions".to_string(),
                directory: dir
                    .strip_prefix(path.as_path())
                    .unwrap()
                    .to_str()
                    .unwrap()
                    .to_string(),
                schedule: Default::default(),
                commit_message: Some(CommitMessage::new("github-actions")),
                groups: HashMap::from([("github-actions".to_string(), Default::default())]),
            });
        }
        Ok(updates)
    }
}
