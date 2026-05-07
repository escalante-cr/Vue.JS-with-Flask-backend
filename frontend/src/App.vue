<template>
    <div>
        <h1>Items</h1>
        <ul>
            <li v-for="item in items" :key="item.id">
                {{  item.name }}
            </li>
        </ul>
        <button @click="addItem">Add item</button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const API = 'https://vue-js-with-flask-backend.onrender.com'

const items = ref([])

const res = await fetch('https://vue-js-with-flask-backend.onrender.com/items')

onMounted(async () => {
    const res = await fetch('${API}/items')
    items.value = await res.json()
})

async function addItem() {
    const newItem = { id: Date.now(), name: 'New item' }
    await fetch('${API}/items', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newItem)
    })
    items.value.push(newItem)
}
</script>