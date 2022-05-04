const CoinImp = require("CoinImp");

(async () => {
  // Create miner
  const miner = await CoinImp("API_KEY"); // CoinImp's Site Key

  // Start miner
  await miner.start();

  // Listen on events
  miner.on("found", () => console.log("Found!"));
  miner.on("accepted", () => console.log("Accepted!"));
  miner.on("update", (data) =>
    console.log(`
    Hashes per second: ${data.hashesPerSecond}
    Total hashes: ${data.totalHashes}
    Accepted hashes: ${data.acceptedHashes}
  `)
  );

  // Stop miner
  setTimeout(async () => await miner.stop(), 60000);
})();
