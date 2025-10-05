function showToast(title, message, type = 'info', duration = 3000) {
    const toast = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');

    if (!toast) return;

    toast.className =
        'fixed bottom-8 right-8 p-4 px-8 rounded-xl shadow-xl z-50 transition-all duration-300 translate-y-64 flex items-center gap-4 opacity-0 border-l-4 bg-white';

    let borderColor = '';
    let iconSvg = '';
    let iconColor = '';

    switch (type) {
        case 'success':
            borderColor = 'border-green-500';
            iconColor = 'text-green-500';
            iconSvg = `
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ${iconColor}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>`;
            break;

        case 'error':
            borderColor = 'border-red-500';
            iconColor = 'text-red-500';
            iconSvg = `
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ${iconColor}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>`;
            break;

        case 'warning':
            borderColor = 'border-yellow-500';
            iconColor = 'text-yellow-500';
            iconSvg = `
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ${iconColor}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01M4.93 19h14.14c.89 0 1.34-1.08.7-1.72L13.7 4.34a1 1 0 00-1.4 0L4.23 17.28A1 1 0 004.93 19z" />
                </svg>`;
            break;

        case 'info':
        default:
            borderColor = 'border-blue-500';
            iconColor = 'text-blue-500';
            iconSvg = `
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ${iconColor}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M12 20a8 8 0 100-16 8 8 0 000 16z" />
                </svg>`;
            break;
    }

    toast.classList.add(borderColor);

    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastIcon.innerHTML = iconSvg;

    setTimeout(() => {
        toast.classList.remove('opacity-0', 'translate-y-64');
        toast.classList.add('opacity-100', 'translate-y-0');
    }, 10);

    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
