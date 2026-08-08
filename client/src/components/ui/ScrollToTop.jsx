import { useEffect, useState } from 'react';
import { FiChevronUp } from 'react-icons/fi';

export default function ScrollToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const handler = () => setVisible(window.scrollY > 400);
    window.addEventListener('scroll', handler);
    return () => window.removeEventListener('scroll', handler);
  }, []);

  return (
    <button
      type="button"
      onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
      className={`fixed bottom-6 right-6 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full bg-primary text-white shadow-soft transition-opacity ${visible ? 'opacity-100' : 'pointer-events-none opacity-0'}`}
      aria-label="Scroll to top"
    >
      <FiChevronUp size={20} />
    </button>
  );
}
