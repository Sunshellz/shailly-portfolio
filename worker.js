export default {
  async fetch(request, env) {
    const response = await env.ASSETS.fetch(request);
    if (response.status === 404) {
      const url = new URL(request.url);
      url.pathname = '/404.html';
      const notFound = await env.ASSETS.fetch(url);
      return new Response(notFound.body, {
        status: 404,
        headers: notFound.headers
      });
    }
    return response;
  }
};
