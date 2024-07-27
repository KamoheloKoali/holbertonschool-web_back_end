export default function guardrail(mathFunction) {
  try {
    const queue = [mathFunction(), 'Guardrail was processed'];
    return queue;
  } catch (e) {
    const msg = `Error: ${e.message}`;
    const queue = [msg, 'Guardrail was processed'];
    return queue;
  }
}
