import React from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import { CiSettings } from "react-icons/ci";

const SessionDropdown = ({ handleLoadAll, handleLoadPreviousSession }) => {
  return (
    <Dropdown>
      <Dropdown.Toggle variant="secondary" id="dropdown-basic">
        <CiSettings/>
      </Dropdown.Toggle>

      <Dropdown.Menu>
          <Dropdown.Item
            onClick={() => handleLoadPreviousSession()}
          >
            Load Previous Sessions
          </Dropdown.Item>
          <Dropdown.Item
            onClick={() => handleLoadAll()}
          >
            Load All Sessions
          </Dropdown.Item>

      </Dropdown.Menu>
    </Dropdown>
  );
};

export default SessionDropdown;