/// <reference types="cypress" />

describe('Teste Funcional de Login', () => {
    it('Deve realizar login com sucesso', () => {
        cy.visit('http://localhost:3000');
        cy.get('[data-test="username"]').type('william@bhzconnection.org.br');
        cy.get('[data-test="password"]').type('password123');
        cy.get('.MuiButtonBase-root').click();
        cy.get('.css-1v45ur3-MuiTypography-root').should('contain', 'Sistema de');

        //Navegação na tela
        cy.get(':nth-child(6) > .MuiPaper-root > .MuiCardContent-root').click();
        cy.get('.css-xe42rm > .MuiBox-root > .MuiButtonBase-root').click();
        cy.get('input#\\:r0\\:').type('01-08-2023');
        cy.get('input#\\:r1\\:[name="end_date"]').type('01-12-2023');
        cy.get('input#\\:r2\\:[name="class_shift"]').type('Integral');
        cy.get('.MuiButton-containedPrimary').click();
        cy.get('.css-xe42rm > .MuiTypography-root').should('contain', 'Lista de Períodos Letivos');
    });

});