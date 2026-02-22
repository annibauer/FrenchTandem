import React from "react";

const HighlightedText = ({ text }) => {
  const renderWithHighlights = (text) => {
    const elements = [];
    let inHighlight = false;
    let buffer = '';

    for (let i = 0; i < text.length; i++) {
      const char = text[i];

      if (char === '*') {
        if (buffer) {
          elements.push(
            <span
              key={elements.length}
              style={{ color: inHighlight ? 'red' : 'black' }}
            >
              {buffer}
            </span>
          );
          buffer = '';
        }
        inHighlight = !inHighlight; // Toggle highlighting
      } else {
        buffer += char;
      }
    }

    // Push any remaining text
    if (buffer) {
      elements.push(
        <span
          key={elements.length}
          style={{ color: inHighlight ? 'red' : 'black' }}
        >
          {buffer}
        </span>
      );
    }

    return elements;
  };

  return <div>{renderWithHighlights(text)}</div>;
};

export default HighlightedText;