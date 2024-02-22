use clap::Parser;

mod cmd;
mod gen;
mod proc;
mod schema;
mod utils;

use self::cmd::Cmd;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let cmd = Cmd::parse();
    cmd.run().await
}
