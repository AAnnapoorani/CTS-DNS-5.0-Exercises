export function handleError(error) {

  console.error('Global Error:', error)

  alert(error.message || 'Unexpected Error')
}