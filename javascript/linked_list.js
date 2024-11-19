/**
 * Represents a node for singly-linked lists.
 */
class SinglyLinkedNode
{
    /**
     * Creates a node that holds [data] and points to [next].
     *
     * @param {*} data
     * @param {SinglyLinkedNode} next
     */
    constructor(data, next=null)
    {
        this.data = data;
        this.next = next;
    }
}

/**
 * Represents a singly-linked list. Provides searching, inserting, and deleting
 * methods.
 */
class SinglyLinkedList
{
    /**
     * Creates a singly-linked list head that holds [data] and points to [next].
     *
     * @param {*} data
     */
    constructor(data)
    {
        this.head = new SinglyLinkedNode(data);

        this.length = 1;
    }

    /**
     * Searches for a node with [data] in it, which is returned. If not found,
     * then [null] is given.
     * 
     * Time complexity - O(N), where N is the list length.
     * Space complexity - O(1).
     * 
     * @param {*} data 
     */
    search(data)
    {
        let old_node = this.head;

        // Iterates over the list.
        while (old_node !== null)
        {
            if (old_node.data === data)
            {
                return old_node;
            }

            old_node = old_node.next;
        }

        return null;
    }

    /**
     * Inserts, at position [index], a node containing [data].
     * 
     * Time complexity - O(N), where N is the list length.
     * Space complexity - O(1).
     * 
     * @param {*} data
     * @param {number} index
     */
    insert(data, index)
    {
        // Ensures [index] is the right type.
        if (typeof index !== "number")
        {
            throw new TypeError(`"${index}" is not a number.`);
        }

        // Ensures [index] is an integer.
        if (index != parseInt(index))
        {
            throw new TypeError(`"${index}" is not an integer.`);
        }

        // Ensures [index] is big enough.
        if (index < 0)
        {
            throw new RangeError(`Index "${index}" must not be negative.`);
        }

        // Inserts a node at the front.
        if (index === 0)
        {
            let new_node = new SinglyLinkedNode(data, this.head);

            this.head = new_node;

            this.length++;

            return;
        }

        // Ensures the [index] isn't too big.
        if (index > this.length)
        {
            throw new RangeError(`Index "${index}" is too big. It must be smaller than or equal to the list length: "${this.length}".`);
        }

        let old_node = this.head;
        let i = 0;

        // Iterates over the list until either the end or a node at an [index]
        // is hit.
        while (true)
        {
            if (old_node === null)
            {
                return;
            }

            if (i === index - 1)
            {
                break;
            }

            old_node = old_node.next;
            i++;
        }

        // Creates a new node that points to the old node that used to be at an
        // [index].
        let new_node = new SinglyLinkedNode(data, old_node.next);

        old_node.next = new_node;

        this.length++;
    }

    /**
     * Deletes, at position [index], a node containing [data].
     * 
     * Time complexity - O(N), where N is the list length.
     * Space complexity - O(1).
     * 
     * @param {*} data
     * @param {number} index
     */
    delete(index)
    {
        // Ensures [index] is the right type.
        if (typeof index !== "number")
        {
            throw new TypeError(`"${index}" is not a number.`);
        }

        // Ensures [index] is an integer.
        if (index != parseInt(index))
        {
            throw new TypeError(`"${index}" is not an integer.`);
        }

        // Ensures [index] is big enough.
        if (index < 0)
        {
            throw new RangeError(`Index "${index}" must not be negative.`);
        }

        // Deletes a node at the front.
        if (index === 0)
        {
            this.head = this.head.next;

            this.length--;

            return;
        }

        // Ensures the [index] isn't too big.
        if (index >= this.length)
        {
            throw new RangeError(`Index "${index}" is too big. It must be smaller than the list length: "${this.length}".`);
        }

        let old_node = this.head;
        let i = 0;

        // Iterates over the list until either the end or a node at an [index]
        // is hit.
        while (true)
        {
            if (old_node === null)
            {
                return;
            }

            if (i === index - 1)
            {
                break;
            }

            old_node = old_node.next;
            i++;
        }

        old_node.next = old_node.next.next;

        this.length--;
    }
}

