const fsa = require("fs/promises");
const path = require("path");
const { exec } = require("child_process");

main();

const mp3Regex = /^(.*).mp3$/i;
async function main() {
	const dirname = process.argv[2] || ".";
	const dirResult = await fsa.readdir(dirname, { withFileTypes: true });
	for (const dirent of dirResult) {
		if (dirent.isDirectory()) {
			continue;
		}

		const filePath = path.join(dirname, dirent.name);

		const result = mp3Regex.exec(filePath);
		if (result == null) {
			continue;
		}

		const newName = result[1] + ".wav";
		try {
			await convertToWav(filePath, newName);
		} catch (e) {
			console.error(`Error converting ${filePath} to wav: ${e}`);
		}
	}
}

function convertToWav(filePath, newPath) {
	return new Promise((res, rej) => {
		exec(`ffmpeg -i ${filePath} ${newPath}`, (error, stdout, stderr) => {
			if (error) {
				rej(`ffmpeg execution error: ${error}`);
				return;
			}

			res(stdout);
		});
	});
}
