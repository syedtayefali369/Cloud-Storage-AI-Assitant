import { useState, useEffect } from 'react';
import axios from 'axios';

const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';

export default function Home() {
  const [form, setForm] = useState({ name: '', email: '', password: '' });
  const [token, setToken] = useState<string>('');
  const [user, setUser] = useState<any>(null);
  const [mode, setMode] = useState<'login'|'register'>('login');

  useEffect(() => {
    const t = localStorage.getItem('token');
    if (t) {
      setToken(t);
      getProfile(t);
    }
  }, []);

  const handle = (e: any) => setForm({ ...form, [e.target.name]: e.target.value });

  const register = async () => {
    try {
      await axios.post(`${API}/api/users/register`, form);
      alert('Registered! Now switch to login.');
      setMode('login');
    } catch (err: any) {
      alert(err.response?.data?.message || 'Error');
    }
  };

  const login = async () => {
    try {
      const { data } = await axios.post(`${API}/api/users/login`, { email: form.email, password: form.password });
      localStorage.setItem('token', data.token);
      setToken(data.token);
      await getProfile(data.token);
    } catch (err: any) {
      alert(err.response?.data?.message || 'Error');
    }
  };

  const getProfile = async (t?: string) => {
    try {
      const { data } = await axios.get(`${API}/api/users/profile`, {
        headers: { Authorization: `Bearer ${t || token}` }
      });
      setUser(data);
    } catch (err) {
      console.error(err);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken('');
    setUser(null);
  };

  return (
    <div style={{ fontFamily: 'Inter, system-ui, Arial', display: 'flex', minHeight: '100vh', alignItems: 'center', justifyContent: 'center', background: '#0f172a' }}>
      <div style={{ width: 420, background: '#0b1220', padding: 28, borderRadius: 12, boxShadow: '0 8px 30px rgba(2,6,23,0.7)', color: '#e6eef8' }}>
        <h1 style={{ margin: 0, marginBottom: 10, fontSize: 22 }}>Agency Auth Demo</h1>
        <p style={{ marginTop: 0, color: '#9fb0d6' }}>Next.js + TypeScript · Express · MongoDB · JWT</p>

        {!user && (
          <>
            <div style={{ display: 'grid', gap: 10, marginTop: 12 }}>
              {mode === 'register' && <input name="name" placeholder="Name" value={form.name} onChange={handle} style={inputStyle} />}
              <input name="email" placeholder="Email" value={form.email} onChange={handle} style={inputStyle} />
              <input name="password" placeholder="Password" type="password" value={form.password} onChange={handle} style={inputStyle} />
              <div style={{ display: 'flex', gap: 8 }}>
                {mode === 'register' ? <button onClick={register} style={primaryBtn}>Register</button> : <button onClick={login} style={primaryBtn}>Login</button>}
                <button onClick={() => setMode(mode === 'login' ? 'register' : 'login')} style={ghostBtn}>
                  {mode === 'login' ? 'Need an account?' : 'Already have account?'}
                </button>
              </div>
              <small style={{ color: '#9fb0d6' }}>API: {API}</small>
            </div>
          </>
        )}

        {user && (
          <div style={{ marginTop: 18 }}>
            <h3 style={{ margin: '6px 0' }}>{user.name}</h3>
            <p style={{ margin: 0, color: '#9fb0d6' }}>{user.email}</p>
            <div style={{ marginTop: 12, display: 'flex', gap: 8 }}>
              <button onClick={logout} style={primaryBtn}>Logout</button>
              <button onClick={() => getProfile()} style={ghostBtn}>Refresh</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const inputStyle: any = {
  padding: '10px 12px',
  borderRadius: 8,
  border: '1px solid rgba(255,255,255,0.06)',
  background: '#071029',
  color: '#e6eef8',
  outline: 'none'
};

const primaryBtn: any = {
  padding: '10px 12px',
  borderRadius: 8,
  border: 'none',
  background: '#2563eb',
  color: 'white',
  cursor: 'pointer',
  flex: 1
};

const ghostBtn: any = {
  padding: '10px 12px',
  borderRadius: 8,
  border: '1px solid rgba(255,255,255,0.06)',
  background: 'transparent',
  color: '#9fb0d6',
  cursor: 'pointer'
};
