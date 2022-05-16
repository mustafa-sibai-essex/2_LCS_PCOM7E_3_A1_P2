const removeConfirmation = () => {
    if (confirm('Are you sure you want to remove this user?')) {
        return true
    } else {
        return false
    }
}