import {Node} from "./singly_linked_list.js"

/**
 * Represents a queue supporting enqueuing, dequeuing, and peeking.
 */
class Queue {
    constructor(item)
    {
        if (item === undefined)
        {
            this.head = null;
            this.length = 0;
        }
        else
        {
            this.head = new Node(item);
            this.length = 1;
        }

        this.tail = this.head;
    }

    peek()
    {
        return this.head;
    }

    dequeue()
    {
        // If the length is 0, then there's nothing to remove.
        if (this.length == 0)
        {
            return null;
        }

        let old_node = this.head;
        // Advances the head forward, effectively deleting it.
        this.head = this.head.next;

        this.length--;

        // Returns the old head.
        return old_node;
    }

    enqueue(item)
    {
        let new_node = new Node(item);

        // If there are no items, then make the new node the first one.
        if (this.tail === null)
        {
            this.head = new_node
            this.tail = this.head;
        }
        // Otherwise, add on to the existing tail and update [tail].
        else
        {
            this.tail.next = new_node;
            this.tail = new_node;
        }

        this.length++;

        return new_node;
    }
}

let queue = new Queue();

queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(4);

console.log(queue.dequeue());