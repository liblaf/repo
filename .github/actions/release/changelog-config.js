"use strict";
const config = require("conventional-changelog-conventionalcommits");

// https://github.com/ellerbrock/conventional-changelog-angular-emoji
// https://github.com/TriPSs/conventional-changelog-action/issues/176#issuecomment-1238331441
module.exports = config({
  types: [
    { type: "feat", section: "✨ Features" },
    { type: "fix", section: "🐛 Bug Fixes" },
    { type: "docs", section: "📖 Documentation" },
    { type: "style", section: "💎 Styles" },
    { type: "refactor", section: "📦 Code Refactoring" },
    { type: "perf", section: "🚀 Performance Improvements" },
    { type: "test", section: "🚨 Tests" },
    { type: "build", section: "👷 Build" },
    { type: "ci", section: "💻 Continuous Integration" },
    { type: "chore", section: "🎫 Chores" },
    { type: "revert", section: "🔙 Reverts" },
  ],
});
