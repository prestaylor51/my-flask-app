import * as React from "react";
import axios from "axios";
import "./App.css";

require('dotenv').config();

interface State {
  code: string;
  santaee: string;
}

class App extends React.Component<any, State> {
    public constructor(props: any) {
        super(props);
        this.state = { 
            code: "",
            santaee: ""
        };
    }

    public componentDidMount = async () => {

    try {
        const data = (await axios.get("/load-data",{})).data;
        console.log("DATA:", data);
    } catch(err) {
        console.log(err);
    }

  };

  getSantaee = async (): Promise<void> => {
      // make the call and retrieve the santaee
      const santaee: string = (await axios.post("/get-my-santaee",{code: this.state.code})).data;
      console.log("RESULT:", santaee);
      this.setState({santaee});
  };

  public render() {
    // const {data} = this.state;
    return <div className="App">
        <h1>Taylor Secret Santa Christmas Draw</h1>
        <p>Enter Code</p>
        <input onChange={(event: React.FormEvent<HTMLInputElement>) => 
            {this.setState({code: event.currentTarget.value});}}>
        </input>
        <button onClick={() => {this.getSantaee()}}>Get Santaee</button>
        <h1>Your Santaee</h1>
        <h2>{this.state.santaee}</h2>
    </div>;
  }
}

export default App;
