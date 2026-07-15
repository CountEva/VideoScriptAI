function getData() {

    return {
        product: document.getElementById("product").value,
        description: document.getElementById("description").value,
        audience: document.getElementById("audience").value,
        goal: document.getElementById("goal").value,
        duration: document.getElementById("duration").value
    };

}

async function sendRequest(endpoint) {

    const response = await fetch(endpoint, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(getData())

    });

    return await response.json();

}

async function generateHook() {

    const data = await sendRequest("/api/generate-hook");

    document.getElementById("hookResult").textContent =
        data.result || data.error;

}

async function generateScript() {

    const data = await sendRequest("/api/generate-script");

    document.getElementById("scriptResult").textContent =
        data.result || data.error;

}

async function generateScenes() {

    const data = await sendRequest("/api/generate-scenes");

    document.getElementById("sceneResult").textContent =
        data.result || data.error;

}

async function generateCTA() {

    const data = await sendRequest("/api/generate-cta");

    document.getElementById("ctaResult").textContent =
        data.result || data.error;

}

async function generateAll() {

    const data = await sendRequest("/api/generate-all");

    if(data.error){

        alert(data.error);

        return;

    }

    document.getElementById("hookResult").textContent = data.hook;

    document.getElementById("scriptResult").textContent = data.script;

    document.getElementById("sceneResult").textContent = data.scenes;

    document.getElementById("ctaResult").textContent = data.cta;

}