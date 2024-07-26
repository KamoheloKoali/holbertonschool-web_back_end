export default function createInt8TypedArray(length, position, value) {
  const typedArr = new Int8Array(() => {
    const arr = [];
    for (let i = 0; i < length; i += 1) {
      if (i !== position) arr.push(0);
      else arr.push(value);
    }
    return arr;
  });

  return typedArr;
}
