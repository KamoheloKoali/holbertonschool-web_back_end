export default function createInt8TypedArray(length, position, value) {
  const typedArr = new Int8Array(length);

  typedArr[position] = value;

  return typedArr;
}
