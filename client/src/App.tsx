import * as React from "react";
import axios from "axios";
import "./App.css";

require('dotenv').config();

interface State {
  data?: string;
}

class App extends React.Component<any, State> {
    public constructor(props: any) {
        super(props);
        this.state = { data: "" };
    }

    public componentDidMount = async () => {

    try {
        console.log(process.env.SERVER)
        let host: string = process.env.SERVER ? process.env.SERVER : "HOST NOT DEFINED";
        const data = (await axios.get(host,{})).data
        console.log("DATA:", data)
        this.setState({data : data.value});
    } catch(err) {
        console.log(err)
    }

  };

  processInput = () => {

  };

  public render() {
    const {data} = this.state;
    return <div className="App">
        <h1>Taylor Secret Santa Christmas Draw</h1>
        <p>Enter your first name</p>
        <input></input>
    </div>;
  }
}

export default App;
