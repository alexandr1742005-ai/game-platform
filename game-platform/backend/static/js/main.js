// Инициализация 3D-сцены (Three.js)
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('webgl-canvas') });
renderer.setSize(window.innerWidth, window.innerHeight);

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
}

animate();

// Бот
async function sendMsg() {
    const input = document.getElementById('chat-input');
    const message = input.value;
    if (!message) return;

    // Отправка сообщения
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message })
    });
    const data = await response.json();

    // Вывод сообщений
    const messagesDiv = document.getElementById('chat-messages');
    messagesDiv.innerHTML += `<p><b>Ты:</b> ${message}</p>`;
    messagesDiv.innerHTML += `<p><b>Бот:</b> ${data.reply}</p>`;
    input.value = '';
}