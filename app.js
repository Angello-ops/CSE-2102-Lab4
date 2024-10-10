const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

let dataStore = [
    { id: 1, name: 'Item 1', description: 'This is item 1' },
    { id: 2, name: 'Item 2', description: 'This is item 2' }
];

app.get('/items', (req, res) => {
    res.status(200).json(dataStore);
});

app.get('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const item = dataStore.find(i => i.id === id);
    if (item) {
        res.status(200).json(item);
    } else {
        res.status(404).json({ message: 'Item not found' });
    }
});

app.post('/items', (req, res) => {
    const newItem = {
        id: dataStore.length + 1,
        name: req.body.name,
        description: req.body.description
    };
    dataStore.push(newItem);
    res.status(201).json(newItem);
});

app.put('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const itemIndex = dataStore.findIndex(i => i.id === id);

    if (itemIndex !== -1) {
        dataStore[itemIndex] = {
            id: id,
            name: req.body.name,
            description: req.body.description
        };
        res.status(200).json(dataStore[itemIndex]);
    } else {
        res.status(404).json({ message: 'Item not found' });
    }
});

app.delete('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const itemIndex = dataStore.findIndex(i => i.id === id);

    if (itemIndex !== -1) {
        dataStore.splice(itemIndex, 1);
        res.status(200).json({ message: 'Item deleted' });
    } else {
        res.status(404).json({ message: 'Item not found' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
