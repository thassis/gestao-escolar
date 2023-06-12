/// <reference types="cypress" />

describe('Teste Funcional de Login', () => {
    it('Deve realizar login com sucesso', () => {
        cy.visit('http://localhost:3000');
        cy.get('[data-test="username"]').type('william@bhzconnection.org.br');
        cy.get('[data-test="password"]').type('password123');
        cy.get('.MuiButtonBase-root').click();
        cy.get('.css-1v45ur3-MuiTypography-root').should('contain', 'Sistema de');
    });

    it('Validando login incorreto', () => {
        cy.visit('http://localhost:3000');
        cy.get('[data-test="username"]').type('william@bhzconnection.org.br1');
        cy.get('[data-test="password"]').type('password123');
        cy.get('.MuiButtonBase-root').click();
        cy.contains('p', 'Invalid email or password').should('be.visible');
    });

    it('Validar senha incorreta', () => {
        cy.visit('http://localhost:3000');
        cy.get('[data-test="username"]').type('william@bhzconnection.org.br');
        cy.get('[data-test="password"]').type('password1234');
        cy.get('.MuiButtonBase-root').click();
        cy.contains('p', 'Invalid email or password').should('be.visible');
    });
});