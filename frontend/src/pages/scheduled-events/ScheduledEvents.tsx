import React, { useEffect } from "react";
import { Box } from '@mui/system';
import { useNavigate } from "react-router-dom";
import { Button, Card, CardActionArea, CardContent, Grid, Paper, Typography } from "@mui/material";
import CardMedia from '@mui/material/CardMedia';

import Header from "shared-components/header/Header";
import { Descricao, GridCards, Subtitle } from "./styles";
import { nextEvent } from "data-front/nextEvent";
import { MenuList } from "data-front/data";
import { STORAGE_EVENT } from "utils/storageKeys";

export interface EventParams {
  name: string;
  id: number;
  description: string;
  date: Date;
}

const ScheduledEvents = () => {
  const navigate = useNavigate();

  const [events, setEvents] = React.useState<EventParams[]>(nextEvent);

  //Importando as imagens
  const NextEvent = require('../../images/evento.jpg');
  const OldEvent = require('../../images/evento4.jpg');
  const RegisterEvent = require('../../images/evento3.jpg');

  //Navegacao
  const onNavigateEventNext = () =>{
    window.location.replace('/events-next');
  }

  const onNavigateEventOld = () =>{
    window.location.replace('/events-old');
  }

  const onNavigateEventRegister = () =>{
    window.location.replace('/events-register');
  }

  const onNavigateEventDetail = (params: EventParams) => {
    navigate('/events-description', { state: params });
  }

  useEffect(() => {
    const valueStr = localStorage.getItem(STORAGE_EVENT);
    console.log(valueStr)

    if(valueStr) {
      const value = JSON.parse(valueStr);
      if(value) {
        setEvents(prev => [...prev, {...value, date: new Date(value.date)}]);
      }
    }
  }, [])

  console.log({events})

  
  return (
    <>
      <Header />
      <Box margin={4}>

        {/* Necessario refatorar esta parte do codigo pois esta estatica */}
        <Box sx={{display: "flex", flexWrap: "wrap", justifyContent: "space-around"}}>

            <Card sx={{ maxWidth: "390px", display: "flex", m: 2 }} onClick={() => onNavigateEventRegister()}>
              <CardActionArea>
                <CardMedia
                  sx={{ minHeight: "200px" }}
                  component={"img"}
                  src={RegisterEvent}

                />
                <CardContent>
                  <Descricao variant="h5" gutterBottom >
                    Cadastrar Eventos
                  </Descricao>
                </CardContent>
              </CardActionArea>
            </Card>
        </Box>

        {/* Próximos Eventos*/}
        <Box ml={7}>
          <Subtitle variant="h4" gutterBottom>
            Próximos eventos
          </Subtitle>
            <Box sx={{display: "flex", flexWrap: "wrap", justifyContent: "space-around"}}>
            {events.map((menu, index) => (
              <Card key={index} sx={{ maxWidth: "390px", display: "flex", m: 2 }} onClick={() => onNavigateEventDetail({name: menu.name, id: menu.id, description: menu.description, date: menu.date})}>
                <CardActionArea>
                  {/*<CardMedia
                    sx={{ minHeight: "200px", maxHeight: "200px", minWidth: "200px", maxWidth: "200px"}}
                    component={"img"}
                    src={menu.image}
                    alt={menu.name}
            />*/}
                  <CardContent>
                    <Descricao variant="h5" gutterBottom >
                      {menu.name}
                    </Descricao>

                    <Descricao variant="body1" gutterBottom >
                      {menu.date.toLocaleDateString()}
                    </Descricao>  
                  </CardContent>
                </CardActionArea>
              </Card>
            ))}
          </Box>
        </Box>
        
        {/* Eventos já ocorridos */}
        <Box ml={7}>
          <Subtitle variant="h4" gutterBottom>
            Eventos Antigos
          </Subtitle>
            <Box sx={{display: "flex", flexWrap: "wrap", justifyContent: "space-around"}}>
            {events.map((menu, index) => (
              <Card key={index} sx={{ maxWidth: "390px", display: "flex", m: 2 }}>
                <CardActionArea>
                  {/*<CardMedia
                    sx={{ minHeight: "200px", maxHeight: "200px", minWidth: "200px", maxWidth: "200px"}}
                    component={"img"}
                    src={menu.image}
                    alt={menu.name}
            />*/}
                  <CardContent>
                    <Descricao variant="h5" gutterBottom >
                      {menu.name}
                    </Descricao>
                  </CardContent>
                </CardActionArea>
              </Card>
            ))}
          </Box>
        </Box>
      </Box>
    </>
  );
};

export default ScheduledEvents;
