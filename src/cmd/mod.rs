use std::path::PathBuf;

use clap::Parser;

use crate::{gen::Generator, schema::Config};

#[derive(Debug, Parser)]
pub struct Cmd {
    #[arg(default_value = ".")]
    dest: PathBuf,
}

impl Cmd {
    pub async fn run(&self) -> anyhow::Result<()> {
        let mut cfg = Config {
            version: 2,
            updates: vec![],
        };
        let generators: [&dyn Generator; 2] = [&crate::gen::Cargo, &crate::gen::GitHubActions];
        for gen in generators {
            let updates = gen.gen(self.dest.as_path())?;
            cfg.updates.extend(updates);
        }
        cfg.save(self.dest.join(".github").join("dependabot.yaml").as_path())
            .await?;
        Ok(())
    }
}
