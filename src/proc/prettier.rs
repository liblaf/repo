use std::{borrow::Cow, process::Stdio};

use tokio::{io::AsyncWriteExt, process::Command};

pub async fn prettier_yaml(contents: &'_ str) -> anyhow::Result<Cow<'_, str>> {
    match prettier_unsafe(contents, "yaml").await {
        Ok(s) => Ok(Cow::Owned(s)),
        Err(_) => Ok(Cow::Borrowed(contents)),
    }
}

async fn prettier_unsafe(contents: &str, parser: &str) -> anyhow::Result<String> {
    let mut cmd = Command::new("prettier");
    cmd.args(["--parser", parser])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::inherit());
    let mut child = cmd.spawn()?;
    let stdin = child.stdin.as_mut().unwrap();
    stdin.write_all(contents.as_bytes()).await?;
    let output = child.wait_with_output().await?;
    anyhow::ensure!(output.status.success());
    Ok(String::from_utf8(output.stdout)?)
}
