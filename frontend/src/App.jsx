import React from "react";
import GlobalStyles from "./styles/global";
import { Container, Content } from "./styles/index"
import Upload from "./components/Upload";
import { uniqueId } from 'lodash';

import api from './services/api'
import TransferList from "./components/TransferList";

class App extends React.Component {
  state = {
    uploadedFiles: []
  }
  
  handleUpload = files => {
    const uploadedFiles = files.map(file => ({
      file,
      id: uniqueId(),
      name: file.name
    }))
    
    this.setState({
      uploadedFiles: this.state.uploadedFiles.concat(uploadedFiles)
    })

    uploadedFiles.forEach(this.processUpload)

  };

  processUpload = (uploadedFile) => {
    const data = new FormData();
    data.append('file', uploadedFile.file, uploadedFile.name)

    api.post('upload', data ).then(res => console.log(res))
  }

  render(){
    return (
        <Container>
          <GlobalStyles/>
          <Content>
            <Upload onUpload={this.handleUpload}/>
            <TransferList/>
          </Content>
        </Container>
    );

  }
}

export default App;
