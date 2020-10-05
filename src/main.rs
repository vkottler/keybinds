use std::path::PathBuf;
use structopt::StructOpt;

enum ManifestFormat {
    YAML,
    JSON,
}

#[derive(Debug, StructOpt)]
/// A tool for interacting with keybind manifests.
struct Opt {
    #[structopt(parse(from_os_str))]
    /// Path to the manifest configuration.
    manifest: PathBuf,
}

fn main() {
    let opt = Opt::from_args();
    println!("{:?}", opt);

    println!("{:?}", opt.manifest.as_path());
}
