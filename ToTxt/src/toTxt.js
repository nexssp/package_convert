const {
  nxsError,
} = require(`${process.env.NEXSS_PACKAGES_PATH}/Nexss/Lib/NexssLog.js`);

const NexssIn = require(`${process.env.NEXSS_PACKAGES_PATH}/Nexss/Lib/NexssIn.js`);
let NexssStdout = NexssIn();

process.chdir(NexssStdout.cwd);

function replaceExtension(filename, extension) {
  var pos = filename.lastIndexOf(".");
  return filename.substr(0, pos < 0 ? filename.length : pos) + extension;
}
const availableTypes = [".pdf"];
if (!NexssStdout.nxsIn) {
  nxsError("Add files to be converted: " + availableTypes.join(", "));
  process.exit(1);
}

const cp = require("child_process");
const path = require("path");
const fs = require("fs");
let result = [];
let exists = [];
let errors = [];

NexssStdout.nxsIn.forEach((element) => {
  const extension = path.extname(element);

  if (!availableTypes.includes(extension)) {
    nxsError(
      "Convert/ToTxt converts these file types: " +
        availableTypes.join(", ") +
        ". You passed: " +
        element
    );
    process.exit(1);
  }

  const destination = replaceExtension(element, ".txt");
  if (!NexssStdout.convertForce && fs.existsSync(destination)) {
    exists.push(destination);
    return;
  }
  switch (extension) {
    case ".pdf":
      try {
        const res = cp.execSync(`pdftotext.exe "${element}"`).toString();
        if (res) console.log(res);
        result.push(destination);
      } catch (error) {
        errors.push(error.message);
        nxsError(error.message);
      }
      break;
    case ".txt":
      break;
    default:
      nxsError(
        `Extension ${extension} is not yet recognized by nexss Convert/ToTxt`
      );
      break;
  }
});
NexssStdout.nxsOut = result;
if (exists.length > 0) NexssStdout.nxsOut_1 = exists;
if (errors.length > 0) NexssStdout.nxsOut_2 = errors;
NexssStdout.nxsInfo = {
  nxsOut: "converted files",
  nxsOut_1: "already exists",
  nxsOut_2: "errors",
};
delete NexssStdout.nxsIn;
delete NexssStdout.resultField_1;
process.stdout.write(JSON.stringify(NexssStdout));
