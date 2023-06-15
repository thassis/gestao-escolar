const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
  "exclude": [
    "cypress",
    "cypress.config.ts" // Adicione essa linha
  ]
});
