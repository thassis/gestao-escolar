/// <reference types="cypress" />

describe('Teste Funcional de Login', () => {
    it('Deve realizar login com sucesso', () => {
        cy.visit('http://localhost:3000');
        cy.get('[data-test="username"]').type('william@bhzconnection.org.br');
        cy.get('[data-test="password"]').type('password123');
        cy.get('.MuiButtonBase-root').click();
        cy.get('.css-1v45ur3-MuiTypography-root').should('contain', 'Sistema de');

        //Navegação na tela
        cy.get(':nth-child(5) > .MuiPaper-root > .MuiCardContent-root').click();
        cy.get(':nth-child(1) > .MuiPaper-root > .MuiButtonBase-root > .MuiCardMedia-root').click();
        cy.get('input#\\:r0\\:').type('Tecnologia BLA')
        cy.get('[data-test="date"]').type('2023-05-01');
        cy.get('[data-test="description_event"]').type('bla bla bla');
        cy.get('.css-xi606m > .MuiButtonBase-root').click();
        cy.get(':nth-child(2) > .MuiTypography-h4').should('contain', 'Próximos eventos');
    });

});