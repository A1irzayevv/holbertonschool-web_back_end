function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch(() => {
      console.log('Got a response from the API');
      const error = Promise.reject(new Error());
      return error;
    });
}

export default handleResponseFromAPI;
