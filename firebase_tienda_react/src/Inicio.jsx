import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import { NavBar } from './componets/nav/nav_manu';
import { Inicio2 } from './componets/inicio2';
import { ListaProductosUSer } from './componets/productos/lista_producto_user';


const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

export const Inicio=()=> {
  return (<>
    <Box sx={{width:1}}>
      <Grid container spacing={1}
            direction="row"
            justifyContent="space-between"
            alignItems="stretch">
        <Grid xs={2}>
            <Item>
                <NavBar/>
            </Item>
        </Grid>
        <Grid xs={4}>
                <Item>
                    <Inicio2/>
                </Item>  
        </Grid>
        <Grid xs={5}>
                <Item>
                    <ListaProductosUSer/> 
                </Item> 
        </Grid>             
        
        
      </Grid>
    </Box>
    </>
  );
}