import React, { Component } from "react";
import { Container, StyledCard, StyledList, Button, Text } from './styles'
import api from '../../services/api'


export default class TransferList extends Component {
  state = {
    responseFiles: []
  }
  getTransfers = () => {
    // const data = new FormData();
    // data.append('file', uploadedFile.file, uploadedFile.name)

    api.get('list_all').then(res => {
      this.setState({ responseFiles: res.data.data })
    })
  }

  render() {
    const { responseFiles = [] } = this.state

    console.log(this.state)
    return (
      <Container>

        <Button onClick={this.getTransfers}> Transações </Button>
        <StyledList >

          {responseFiles.map(({
            store_owner, store_name, card, cpf, date, hour, id, trans_type, value}, key) => ( 
          
          <StyledCard key={key} >
              <Text>{store_owner}</Text>
               <Text>{store_name}</Text>
               <Text>{card}</Text>
               <Text>{cpf}</Text>
               <Text>{date}</Text>
               <Text>{hour}</Text>
               <Text>{trans_type}</Text>
               <Text>{value}</Text>
          </StyledCard>
          ))}
        </StyledList>
      </Container>
    )


  }

}
