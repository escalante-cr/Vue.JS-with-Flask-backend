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

const items = ref([])

onMounted(async () => {
    const res = await fetch('http://localhost:5000/items')
    items.value = await res.json()
})

async function addItem() {
    const newItem = { id: Date.now(), name: 'New item' }
    await fetch('http://localhost:5000/items', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newItem)
    })
    items.value.push(newItem)
}
</script>