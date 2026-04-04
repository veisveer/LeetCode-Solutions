function decodeCiphertext(encodedText: string, rows: number): string {
	let columns = encodedText.length / rows;
	let output = "";

	for (let start = 0; start < columns; start++) {
		output += encodedText[start];

		let index = start;
		while (index < encodedText.length) {
			index += columns + 1;
			if (index < encodedText.length) {
				output += encodedText[index];
			} else {
				break;
			}

		}
	}
	return output.trimEnd();
};