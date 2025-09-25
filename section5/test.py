import heapq  # For managing largest negative adjustments efficiently

def optimizeInventory(inventoryAdjustments):
    # Current inventory level
    current_inventory = 0
    
    # Counter for applied adjustments
    applied_count = 0
    
    # Max-heap (using min-heap with negative values in Python)
    negatives_heap = []
    
    # Process each adjustment
    for adj in inventoryAdjustments:
        # Apply the adjustment
        current_inventory += adj
        applied_count += 1
        
        # If it's a negative adjustment, push it to heap
        if adj < 0:
            heapq.heappush(negatives_heap, adj)  # push negative values
        
        # If inventory goes below 0 → undo one worst negative adjustment
        if current_inventory < 0:
            largest_negative = heapq.heappop(negatives_heap)  
            # Undo it: subtracting negative = adding back
            current_inventory -= largest_negative
            applied_count -= 1  # adjustment undone
    
    return applied_count


# -------------------------------
# User Input Handling
# -------------------------------
if __name__ == "__main__":
    # Take number of adjustments
    n = int(input("Enter number of adjustments: "))
    
    # Read adjustments into a list
    adjustments = []
    for i in range(n):
        val = int(input(f"Enter adjustment {i+1}: "))
        adjustments.append(val)
    
    # Call the function and print result
    result = optimizeInventory(adjustments)
    print("Maximum number of adjustments applied:", result)
