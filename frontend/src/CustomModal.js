import React from "react";

class CustomModal extends React.Component {
  handleRemove = () => {
    this.props.onRemove();
  };

  handleSave = () => {
    this.props.onSave({});
  };

  render() {
    const { start, end } = this.props;
    return (
      <div className="customModal">
        <div className="customModal__text">
          <div>{`${start.format("Do MMM. kk:mm")} (${start.format("Z")})`}</div>
          <div>{`${end.format("Do MMM. kk:mm")} (${end.format("Z")})`}</div>
        </div>
        <div className="flex-button-container">

        <div className="flex-button">
            <button className="button-red" onClick={this.handleRemove}>
              delete
            </button>
          </div>

          <div className="flex-button">
            <button onClick={this.handleSave}>cancel</button>
          </div>

        </div>
      </div>
    );
  }
}

export default CustomModal;
