# Changelog

## 0.1.0 (2024-09-10)

### ✨ Features

- add command line interface for generating and saving updates ([bbdde9f](https://github.com/liblaf/repo/commit/bbdde9f349e0dcd21066e3b25dd458b71144fdbe))
- add GitHub Actions workflow for installing packages ([fa95f53](https://github.com/liblaf/repo/commit/fa95f53e6b090913f5da7d89bfac4094f79d1614))
- **ci:** remove poetry-lock from pre-commit hooks ([96d206f](https://github.com/liblaf/repo/commit/96d206fc5315856600fe6d202ce39fd976576a9e))
- **common:** add Renovate configuration file ([68b9ef3](https://github.com/liblaf/repo/commit/68b9ef36db3ab8a986932ccbae0452e6d8cd6647))
- **install:** improve Homebrew installation script ([8d8641e](https://github.com/liblaf/repo/commit/8d8641e2c6ba5a5e1a3f2edd9660f596d27cb8e5))

### 🐛 Bug Fixes

- **.github/actions/install/scripts/brew.sh:** update path to use brew command ([af9ce90](https://github.com/liblaf/repo/commit/af9ce90dfebe0d81d99f17f3ede8509550b4e31b))
- **.github/actions/install/scripts/other/pch.sh:** update architecture check in pch.sh script ([c2f4ee6](https://github.com/liblaf/repo/commit/c2f4ee6b953911ac0e8d78f1ee2201615d058a46))
- **.github/actions/release/main.sh:** fix handling of files in release script ([d85f0bb](https://github.com/liblaf/repo/commit/d85f0bb9b51ac1ecc2cd9554f4b8b0b4aa7fc7ba))
- **.github/workflows/repo.yaml:** update Git user name and email configuration ([a0c425e](https://github.com/liblaf/repo/commit/a0c425e8e0548ee729dfde36820d16b2bc0f2a85))
- add --clobber flag to overwrite existing files when downloading release assets ([983a3bf](https://github.com/liblaf/repo/commit/983a3bf3fc5f25a6876ec1bf9bfbbea484f339ff)), closes [#5](https://github.com/liblaf/repo/issues/5)
- add stdout parameter to subprocess.run for downloading files ([e078cc6](https://github.com/liblaf/repo/commit/e078cc636d262e250893c0b58238b3e75ddaf461))
- add support for Linuxbrew package manager ([1a74364](https://github.com/liblaf/repo/commit/1a7436491d567d615ef928453dd2baa042c3811a))
- **ci:** setup Git configuration for GitHub Actions ([014a212](https://github.com/liblaf/repo/commit/014a2121c2af61047dacb7593ef392ae7654603b))
- **common/.github/blunderbuss.yml:** add renovate[bot] to ignored authors ([4eff1b9](https://github.com/liblaf/repo/commit/4eff1b940a8dcfcdd6571eeb21ec19fcb23ea5a4))
- **common:** add dependabot workflow and update github.sh ([9efadad](https://github.com/liblaf/repo/commit/9efadadf6f84ec10c0fcd15aaf48c5471b29fe0b))
- **common:** add stale workflow and update Makefile ([d66f2c4](https://github.com/liblaf/repo/commit/d66f2c4fbfb897e2211eccbc6806999c0c468fd8))
- **common:** disable isAdminEnforced for main branch and skip shellcheck in pre-commit config ([5f540b3](https://github.com/liblaf/repo/commit/5f540b3aaf38d8d7556f85e17b8e2ced6aa5fcc9))
- **common:** remove branch protection rule and update branch protection settings ([843b199](https://github.com/liblaf/repo/commit/843b1996cb253fde1a79f0eb6b25853d3e08bafd))
- **common:** remove deprecated dependabot configuration ([634193f](https://github.com/liblaf/repo/commit/634193f1b72bc4d9c20e995e255cd1e45c1f7a9c))
- **common:** remove unnecessary app parameter in setting GH_TOKEN secret ([a284412](https://github.com/liblaf/repo/commit/a284412f8712457fd220477b43ad5947a297f541))
- **common:** update Makefile to improve file copying process ([00a6eb1](https://github.com/liblaf/repo/commit/00a6eb131b674cf249cc6216b95289f41b3a51c7))
- correct platform check for ARM64 macOS ([7ec68d1](https://github.com/liblaf/repo/commit/7ec68d1b730271fba352d3c5658ed53658ec457e))
- exclude additional CI bot from PR assignment ([87f368c](https://github.com/liblaf/repo/commit/87f368ced7debeeb3379640d668aac7627e5fc66))
- exclude specific files from pre-commit checks ([e97e3c2](https://github.com/liblaf/repo/commit/e97e3c28342deac450a46abb5993c90291469fbb))
- handle CHANGELOG variable presence correctly ([38498a5](https://github.com/liblaf/repo/commit/38498a528cafeeb1036a57686422252d206ca316))
- improve GitHub release deletion process ([cb6e809](https://github.com/liblaf/repo/commit/cb6e8095df71852f8eeb9e002e87a56cb562bd6e))
- improve handling of changelog file to prevent index out of range error ([44487da](https://github.com/liblaf/repo/commit/44487daf65316779c5c8bda5dd13d1d46cb5657b))
- **install:** use absolute path for sourcing other scripts ([a69b485](https://github.com/liblaf/repo/commit/a69b48544677910b8af05d61d2b00fc950a01164))
- **release:** correct spelling of 'pre-release' and update 'main.sh' script ([9872157](https://github.com/liblaf/repo/commit/98721577050a8dd8617f5a785e564f3bd3992370))
- remove unused imports and functions from release script ([9419bd0](https://github.com/liblaf/repo/commit/9419bd075dcfc21dbcfe0b3f352c5663f20cd5e9))
- rename path.sh to env.sh for clarity ([d31e2f8](https://github.com/liblaf/repo/commit/d31e2f810dcfc6eef2c65ec16ca65e4816046288))
- resolve issue with incorrect data being displayed ([98084cd](https://github.com/liblaf/repo/commit/98084cde6280a72fe446229223a43e71631a0f3b))
- **scripts/sync.sh:** improve error handling in sync script ([9c4d6f5](https://github.com/liblaf/repo/commit/9c4d6f5c7afe012132f87e2f142a9ebd9b1d4e74))
- **scripts:** update cspell initialization script to dynamically include additional ignore paths ([9d0e65a](https://github.com/liblaf/repo/commit/9d0e65a7145c28d313dae52e3ef30083e12f3cc0))
- set correct variable name for destination directory ([fb7912a](https://github.com/liblaf/repo/commit/fb7912a3212997f0dad3a60979fd1335839a1992))
- temporarily disable changelog generation ([6aaf924](https://github.com/liblaf/repo/commit/6aaf92417a80cbef4d7398f4dd6f8e4d1187de3d))
- update changelog generation to use conventional-changelog-cli ([ddaf7aa](https://github.com/liblaf/repo/commit/ddaf7aa1f32b104e53c522dc5b7df8db06ffa977))
- update config file path in release action ([78ee988](https://github.com/liblaf/repo/commit/78ee9882de9b261e8b5fb7e9871a09fb1888fc57))
- update descriptions for package managers in action.yaml ([bf4009b](https://github.com/liblaf/repo/commit/bf4009b3deef103572dd49b507c4c9d0e09c676f))
- update download command in GhRelease class for compatibility ([28d7a95](https://github.com/liblaf/repo/commit/28d7a958c666601d70cced4c6e3e3486b9ec8aef))
- update file path for changelog configuration ([dea1106](https://github.com/liblaf/repo/commit/dea110643cf0680d4a7b764f7d7052c8af08cff8))
- update installation script to correctly set output and pattern for pch on different platforms ([3c87996](https://github.com/liblaf/repo/commit/3c87996346f7b226022474f60d2918f90c41c567))
- update installation scripts and workflow for better platform compatibility ([5465b32](https://github.com/liblaf/repo/commit/5465b32977465070d38868953ac13539a00283f9))
- update npm install command for conventional-changelog-angular-emoji ([b57590b](https://github.com/liblaf/repo/commit/b57590b7c01a36a2d361ba0d2b9bcf98a9f4667c))
- update paths in action.yaml to use pm subdirectory for package manager scripts ([32ca6b7](https://github.com/liblaf/repo/commit/32ca6b76dcf4ac7ec9e99aac7a1ee87edf9956bf))
- update pre-commit configuration to use pipx for installation ([d6ba226](https://github.com/liblaf/repo/commit/d6ba226edd137e9771a5fa6643a0351fc1bf7884))
- update pre-commit hook id for latexindent ([2e17433](https://github.com/liblaf/repo/commit/2e174338333761cfeaca92642ea9185d3cfa7a8a))
- update Python installation process ([e7061aa](https://github.com/liblaf/repo/commit/e7061aa6db0fea34ddb4cd479dc5de5e61f0e38e))
- update release action to include custom changelog config ([f4f3e83](https://github.com/liblaf/repo/commit/f4f3e83c6d27ac8ccc7399348718b48d858c70ae))
- update repository input default value ([15485d6](https://github.com/liblaf/repo/commit/15485d60cb7aa552bf948ed4715078b33fcde072))
- **workflows:** add pipx to the list of tools for job ([0182882](https://github.com/liblaf/repo/commit/0182882b5807b9b3f515627a176414f92d87642c))
- **workflows:** update cron schedule in pre-commit-update.yaml ([6e96e29](https://github.com/liblaf/repo/commit/6e96e29e0a22dc80df95e43d3094943dc6c33577))

### 📚 Documentation

- add README.md with information about repository configuration files and GitHub apps ([b57a472](https://github.com/liblaf/repo/commit/b57a472a2a436d5dfa55474cfddd62ad30e29fdb))
- update README.md with links to config files and GitHub Apps ([0da7967](https://github.com/liblaf/repo/commit/0da7967d16e158171f5be100c7a6fb91ac7ab65f))

### 🏗 Miscellaneous Chores

- add Renovate configuration file ([e7c85f7](https://github.com/liblaf/repo/commit/e7c85f7a1a5b94522a2fee255e15b1fd3fea446e))
- add shellcheck directive to ignore SC2148 in .envrc ([bf1006b](https://github.com/liblaf/repo/commit/bf1006b7d4d9ca8907a3935f4c8b82d1f7eaf0c2))
- **deps:** update eifinger/setup-rye action to v4 ([b31ffe2](https://github.com/liblaf/repo/commit/b31ffe22c8331d072b5c21424e21f08743b0f7c9))
- **deps:** update python docker tag to v3.12.3 ([cbe63cc](https://github.com/liblaf/repo/commit/cbe63cc4cfcf69cab3c2c1d02b91520bfae7a38e))
- **deps:** update python docker tag to v3.12.4 ([519bc92](https://github.com/liblaf/repo/commit/519bc92a4ec53fa479f20959125c6958500648a0))
- **deps:** update python docker tag to v3.12.5 ([8bbf610](https://github.com/liblaf/repo/commit/8bbf610efe543c5028ef19d2137b66e9699fb590))
- remove unnecessary code related to Cargo.toml, command generation, and code formatting ([3e6f672](https://github.com/liblaf/repo/commit/3e6f672ef3d67cb3437371de68847801aa4f82e5))
- **scripts:** add script to clone all GitHub repositories ([d852c44](https://github.com/liblaf/repo/commit/d852c4492cb8391f93bd70f73fb698503e964714))
- update changelog emoji and visibility settings ([a34de65](https://github.com/liblaf/repo/commit/a34de65a97107da994b5c0b69cc7584b70eab093))
- update configuration settings for improved performance ([183600a](https://github.com/liblaf/repo/commit/183600ab6c8307d15b8de99e42b8ea29ace65d69))
- update pre-commit hooks to latest versions ([8a10ec4](https://github.com/liblaf/repo/commit/8a10ec4868c2f0dd305877f23b09f6bcd3106113))

### 💻 Continuous Integration

- add configuration files for auto-label, blunderbuss, and sync-repo-settings ([b6409dc](https://github.com/liblaf/repo/commit/b6409dc8c55de8a88850ee963f55ac1b8b15d993))
- add GitHub release action for automated releases ([1e7ecaa](https://github.com/liblaf/repo/commit/1e7ecaac2730adabec510be1caaab0a5ad546643))
- improve changelog generation by formatting with prettier ([f470b0a](https://github.com/liblaf/repo/commit/f470b0a05b38449bc24f37a72d43a659cde54afb))
- **pre-commit:** update pre-commit hooks ([baa65e4](https://github.com/liblaf/repo/commit/baa65e4b0e22560b3f9efc34d67551b45c55b315))
- **pre-commit:** update pre-commit hooks ([5596e57](https://github.com/liblaf/repo/commit/5596e570867b22f7c8c0afa86a7f6320f0ea2a5a))
- **pre-commit:** update pre-commit hooks ([b9d2381](https://github.com/liblaf/repo/commit/b9d238158f5013ed6753efe1051ac7cf341ecf49))
- **pre-commit:** update pre-commit hooks ([d913f58](https://github.com/liblaf/repo/commit/d913f58114fdd6dac6ee2ce21a5d07d9049a2533))
- **pre-commit:** update pre-commit hooks ([4cb579a](https://github.com/liblaf/repo/commit/4cb579a7583e333f5de43bfc36b038d566eeac6c))
- **pre-commit:** update pre-commit hooks ([9881503](https://github.com/liblaf/repo/commit/988150341dbc2dca46bafbd607e82ad0756860db))
- **pre-commit:** update pre-commit hooks ([16d8adf](https://github.com/liblaf/repo/commit/16d8adf4a2a89cf92f2a14f9efc77fba0bca5923))
- **pre-commit:** update pre-commit hooks ([15b8002](https://github.com/liblaf/repo/commit/15b80025a5ed03ad78961674c85d243c902888a8))
- **pre-commit:** update pre-commit hooks ([7936e94](https://github.com/liblaf/repo/commit/7936e9456092932b0d3c5fbb394bee3babfa4f25))
- **pre-commit:** update pre-commit hooks ([b26557e](https://github.com/liblaf/repo/commit/b26557e84a4984fd54d59405e4341eb924e6cc84))
- **pre-commit:** update pre-commit hooks ([7793b02](https://github.com/liblaf/repo/commit/7793b025295a694500182cc8185786b356cc3c7f))
- **pre-commit:** update pre-commit hooks ([b8329e6](https://github.com/liblaf/repo/commit/b8329e6bbfc16312be48dd1950b9001d917b5706))
- **pre-commit:** update pre-commit hooks ([525df6c](https://github.com/liblaf/repo/commit/525df6c3f5fc6bb1111b426e871daa920e9674e9))
- **pre-commit:** update pre-commit hooks ([1d26761](https://github.com/liblaf/repo/commit/1d267616802397f7926dbf7622f4daeb5122c073))
- **pre-commit:** update pre-commit hooks ([bc39d52](https://github.com/liblaf/repo/commit/bc39d52e42befb85c11fff2df6f9cfb0d713256e))
- **pre-commit:** update pre-commit hooks ([1e6dec8](https://github.com/liblaf/repo/commit/1e6dec898c03bcf226fa6814a40d4b80b4597738))
- **pre-commit:** update pre-commit hooks ([e292a25](https://github.com/liblaf/repo/commit/e292a25a863ef6e9b9b072fb0928e4517c4c8493))
- **pre-commit:** update pre-commit hooks ([a9404c8](https://github.com/liblaf/repo/commit/a9404c876f9d011dde8da89c67796159badca958))
- **pre-commit:** update pre-commit hooks ([71f9796](https://github.com/liblaf/repo/commit/71f9796cb6d6fed357815aa3bb49f3a147948e0d))
- **pre-commit:** update pre-commit hooks ([ca9d297](https://github.com/liblaf/repo/commit/ca9d2971982e211829c553b090aacded1f073e93))
- **pre-commit:** update pre-commit hooks ([7cf7059](https://github.com/liblaf/repo/commit/7cf705940167d4bcbe99b07cd01cfa2d7de266b6))
- **pre-commit:** update pre-commit hooks ([a8f6ae5](https://github.com/liblaf/repo/commit/a8f6ae53651627ebfce762dc9a714800b2b4edc0))
- **pre-commit:** update pre-commit hooks ([0d40ed7](https://github.com/liblaf/repo/commit/0d40ed7bfd38803dd4748dc9fedddab38dc27033))
- **pre-commit:** update pre-commit hooks ([ea12131](https://github.com/liblaf/repo/commit/ea1213153c2349f675928b766be62ec4207683eb))
- **pre-commit:** update pre-commit hooks ([d4fd95a](https://github.com/liblaf/repo/commit/d4fd95afb448be9861b8603e2dbf011575d7eb89))
- **repo:** sync with repo template ([5ac4bc7](https://github.com/liblaf/repo/commit/5ac4bc738b4c09ccba4829a99c8c81d17f3a826d))
- **repo:** sync with repo template ([d51e552](https://github.com/liblaf/repo/commit/d51e5520f9f19300e3446634110fd27b57166cc9))
- **repo:** sync with repo template ([c2f16fa](https://github.com/liblaf/repo/commit/c2f16fa0322cf12e9a7bdd50cf0616921f8308ca))
- **repo:** sync with repo template ([43e4c77](https://github.com/liblaf/repo/commit/43e4c77855bef883f1881d8966ed5cdc095c9716))
- **repo:** sync with repo template ([bf92009](https://github.com/liblaf/repo/commit/bf92009c10057eb7c00cb79d702e2b719de42ac6))
- **repo:** sync with repo template ([46b2a2e](https://github.com/liblaf/repo/commit/46b2a2e9c425f255f1e00af7f16d977fc5e484b6))
- **repo:** sync with repo template ([39e1e4d](https://github.com/liblaf/repo/commit/39e1e4d26800b2f05398405e63da4d95134bd0f3))
- **repo:** sync with repo template ([e02aee3](https://github.com/liblaf/repo/commit/e02aee3d2b33a5bb0213fc1a82446ba481ab2222))
- **repo:** sync with repo template ([e3a6892](https://github.com/liblaf/repo/commit/e3a6892fb5e42d32a49b7d2b667fb5fe448d7855))
- **repo:** sync with repo template ([9e8dd77](https://github.com/liblaf/repo/commit/9e8dd771e95f6c257f87295961d2768dbbbd2643))
- **repo:** sync with repo template ([48faeaf](https://github.com/liblaf/repo/commit/48faeaf0e1b03d0eb8a25f6a2dd2255c459c7035))
- **repo:** sync with repo template ([9d961ac](https://github.com/liblaf/repo/commit/9d961acc906b1e1a923ab1e98df936a7d53c163e))
- **repo:** sync with repo template ([52dbfc0](https://github.com/liblaf/repo/commit/52dbfc01965622566a388bb82554322867bde795))
- **repo:** sync with repo template ([8e849c6](https://github.com/liblaf/repo/commit/8e849c610e57f166fb30e22184f02a2912c03628))
- **repo:** sync with repo template ([ac5e127](https://github.com/liblaf/repo/commit/ac5e1278197a9cab9a72e34ea619df6792c09ea9))
- **repo:** sync with repo template ([45399ab](https://github.com/liblaf/repo/commit/45399abd89bd14652adc257b2dffd30725b22963))
- **repo:** sync with repo template ([b938fa2](https://github.com/liblaf/repo/commit/b938fa268b9cfefc2ef59827187bc024e382b82d))
- **repo:** sync with repo template ([af3ccd4](https://github.com/liblaf/repo/commit/af3ccd4aca128db269b85acb4a9d03eead596656))
- **repo:** sync with repo template ([1c7d280](https://github.com/liblaf/repo/commit/1c7d28092ef552afd71813bbc6d867a306da7e91))
- **repo:** sync with repo template ([dbcdf2e](https://github.com/liblaf/repo/commit/dbcdf2e920b6453e768fc829d4bc18bd0a4007c6))
- **repo:** sync with repo template ([e046323](https://github.com/liblaf/repo/commit/e046323cc271c1d9394207de3d91ee58aaaec959))
- update pre-commit-update and repo workflows to install tools ([9c88ea1](https://github.com/liblaf/repo/commit/9c88ea1d0280a77351d820f4b3fe745f4f79e8bd))
- **workflows:** update test-install workflow to use matrix for different operating systems ([67c982c](https://github.com/liblaf/repo/commit/67c982ca2e93ede5f724d4cf0163372fe5dd63de))