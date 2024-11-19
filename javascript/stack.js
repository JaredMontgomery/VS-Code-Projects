import {SinglyLinkedNode} from "./singly_linked_list.js";

class Stack
{
    /**
     * Creates a stack that holds one item with [data].
     *
     * @param {*} data
     */
    constructor(data)
    {
        this.head = new SinglyLinkedNode(data);

        this.length = 1;
    }

    /**
     * Pushes a new item with [data] on the stack.
     * 
     * @param {*} data 
     */
    push(data)
    {
        let new_node = new SinglyLinkedNode(data, this.head);

        this.head = new_node;

        this.length++;
    }

    /**
     * Pops an item from the stack.
     * 
     * @throws {RangeError} For when there are no items.
     */
    pop()
    {
        if (this.length === 0)
        {
            throw new RangeError(`Can only pop items if length is more than 0.`);
        }

        this.head = this.head.next;

        this.length--;
    }
}

