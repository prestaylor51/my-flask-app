import * as React from "react";
import axios from "axios";
import "./App.css";

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
      const data = (await axios.get("http://localhost:5000/",{})).data
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
