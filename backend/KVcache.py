
from typing import Any, Optional


class KVCache:

    def __init__(self):
        self.store: dict[str, Any] = {}

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache by key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key, or None if not found
        """
        return self.store.get(key, None)

    def put(self, key: str, value: Any) -> bool:
        """Store a key-value pair in the cache.
        
        Args:
            key: The key to store
            value: The value to store
            
        Returns:
            True if the operation was successful
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        self.store[key] = value
        return True
    
    def delete(self, key: str) -> bool:
        """Delete a key-value pair from the cache.
        
        Args:
            key: The key to delete
            
        Returns:
            True if the key was deleted, False if it didn't exist
        """
        if key in self.store:
            del self.store[key]
            return True
        return False
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        self.store.clear()
    
    def size(self) -> int:
        """Get the number of items in the cache.
        
        Returns:
            The number of key-value pairs in the cache
        """
        return len(self.store)