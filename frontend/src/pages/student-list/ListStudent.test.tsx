import "@testing-library/jest-dom/extend-expect";
import React from "react";

import { MemoryRouter } from "react-router-dom";
import { render, screen } from "@testing-library/react";

import ListStudent from "./ListStudent";

describe("ListStudent component", () => {
  it("renders the search input", () => {
    render(
      <MemoryRouter>
        <ListStudent />
      </MemoryRouter>
    );
    const searchInput = screen.getByLabelText("Busca por aluno");
    //assert
    expect(searchInput).toBeInTheDocument();
  });

  it('Make sure the screen has title', () => {
    render(
      <MemoryRouter>
        <ListStudent />
      </MemoryRouter>
    );
    const titleElement = screen.getByText('Lista de Alunos');
    expect(titleElement).toBeInTheDocument();
  });
  
});
