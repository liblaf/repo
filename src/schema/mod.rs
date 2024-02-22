use std::{collections::HashMap, path::Path};

use serde::{Deserialize, Serialize};

#[derive(Clone, Debug, Deserialize, Serialize)]
pub struct Config {
    pub version: i32,
    pub updates: Vec<Update>,
}

#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(rename_all = "kebab-case")]
pub struct Update {
    pub package_ecosystem: String,
    pub directory: String,
    pub schedule: Schedule,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub commit_message: Option<CommitMessage>,
    #[serde(default, skip_serializing_if = "HashMap::is_empty")]
    pub groups: HashMap<String, Group>,
}

#[derive(Clone, Debug, Deserialize, Serialize)]
pub struct Schedule {
    interval: String,
}

impl Default for Schedule {
    fn default() -> Self {
        Self {
            interval: "weekly".to_string(),
        }
    }
}

#[derive(Clone, Debug, Deserialize, Serialize)]
#[serde(rename_all = "kebab-case")]
pub struct CommitMessage {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub prefix: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub prefix_development: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub include: Option<String>,
}

impl CommitMessage {
    pub fn new(name: &str) -> Self {
        Self {
            prefix: Some(format!("build({})", name)),
            prefix_development: Some(format!("build({}-dev)", name)),
            include: Some("scope".to_string()),
        }
    }
}

#[derive(Clone, Debug, Deserialize, Serialize)]
pub struct Group {
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub patterns: Vec<String>,
}

impl Default for Group {
    fn default() -> Self {
        Self {
            patterns: vec!["*".to_string()],
        }
    }
}

impl Config {
    pub async fn save(&self, path: &Path) -> anyhow::Result<()> {
        let contents = serde_yaml::to_string(self)?;
        let contents = crate::proc::prettier::prettier_yaml(contents.as_str()).await?;
        tokio::fs::write(path, contents.as_bytes()).await?;
        Ok(())
    }
}
