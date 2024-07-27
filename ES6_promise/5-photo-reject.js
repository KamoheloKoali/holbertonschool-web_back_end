export default function uploadPhoto(filename) {
  const myPromise = new Promise((reject) => {
    reject(Error(`${filename} cannot be processed`));
  });

  return myPromise;
}
